# Production Source

Production is built from one exact source commit whose identity can be reconstructed later. The source must be on the protected default branch (`main` in the default policy) or identified by an annotated release tag that points to such a commit.

## Eligibility Rule

Accept exactly one of:

1. the exact commit currently reachable from protected `main`; or
2. an annotated release tag whose peeled commit is reachable from protected `main`.

Reject every other source:

- a feature branch, even after a successful preview;
- an unmerged release branch;
- a mutable branch such as `release/latest` or `production`;
- a floating tag;
- a lightweight tag with no tagger/message;
- a working tree with uncommitted or untracked build input;
- a build system that resolved a branch name without pinning the SHA.

The production environment can be protected separately. Restrict it to the allowed branch/tag pattern and, where the platform supports it, require a reviewer. The live environment rule is the authority; this reference defines the release owner's evidence.

## Verify the Commit

```bash
git fetch origin main --tags
SOURCE_SHA="$(git rev-parse "$SOURCE^{commit}")"
git merge-base --is-ancestor "$SOURCE_SHA" origin/main
printf 'source=%s\n' "$SOURCE_SHA"
```

`merge-base --is-ancestor` exits zero only when the source is in `main` history. A source that exists on a remote but not on `main` fails this check.

## Verify the Tag

```bash
git cat-file -t "$TAG"                 # must print: tag
TAG_SHA="$(git rev-parse "$TAG^{commit}")"
git merge-base --is-ancestor "$TAG_SHA" origin/main
git for-each-ref "refs/tags/$TAG" --format='%(objecttype) %(taggername) %(taggerdate:iso-strict) %(*objectname)'
```

An annotated tag records a tag object, tagger, date, and message, and can carry a signature. A lightweight tag lacks those fields, so it is not an auditable release identifier by itself. `^{commit}` peels the annotated tag to the commit that must be checked against `main`.

The tag is created after the source commit is merged to `main`; never tag the feature branch and then merge. If the project signs tags or artifacts, verify the signature or record the missing evidence as a provenance gap.

## Prove the Build Source

The build job must check out the exact eligible SHA, not a branch name that can move between queueing and execution:

```bash
git checkout --detach "$SOURCE_SHA"
git status --porcelain --untracked-files=all
git rev-parse HEAD
```

Any status output means the build input is not the recorded commit; stop and clean or rebuild from a fresh checkout. Record the resolved SHA before the build starts and compare it after checkout. A branch-triggered CI job that fetched later commits is a different source unless the job actually built the recorded SHA.

## Promote, Do Not Rebuild

Build once from the eligible commit. Promote the same immutable artifact and layer environment configuration on top. If a platform cannot promote, rebuilding is allowed only from the same recorded commit and must be recorded as a second artifact with its own digest and build identity; it is not the same artifact.

## Release Record

Record at minimum:

- default branch and protection state observed;
- source ref (branch or tag);
- peeled source commit SHA;
- tag object type, tagger, and date when a tag is used;
- artifact digest and build identity;
- release ID and configuration version;
- production environment and deployment time;
- rollback release ID and artifact;
- verification gaps such as an unreadable protection layer or unsigned tag.

If the source cannot be proven eligible, stop the release. Do not “record an exception” and deploy; route the change back through the mainline integration path.

## Rollback

A rollback targets a previously released artifact whose source was eligible when it shipped. Redeploying that immutable artifact is preferred. A source revert must land through a PR to protected `main`, pass the required checks, and produce a new release ID. Never move a shared tag, force-push `main`, or relabel the broken release as the previous one.

## Done When

The exact source SHA is main-reachable or tag-peeled and main-reachable, the build/artifact identity points to it, and the release record shows no unrecorded source, untrusted tag, or unprotected production path.

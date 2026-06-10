# Automated Multi-Environment Release Pipeline

Modern CI/CD and Release Management architecture demonstrating automated governance, semantic versioning, and environment promotion control.

## Architecture & Governance

### 1. Git & Branching Strategy
* **Trunk-Based Development:** All feature branches target the `main` branch.
* **Branch Protection:** Direct pushes to `main` are disabled. All changes must go through a Pull Request and pass mandated automated status checks.

### 2. Quality Gates (Continuous Integration)
Every Pull Request triggers the CI pipeline (`ci.yml`) which enforces:
* **Linting:** Flake8 syntax and style compliance.
* **Testing:** Pytest execution for regression testing.
* **Compliance:** Verification of PR titles using **Conventional Commits** specification.

### 3. Release Automation & Semantic Versioning
Upon merging compliant code to `main`, the Release Pipeline (`release.yml`) utilizes Google's `release-please` to:
* Parse git history and classify changes (Features vs. Fixes).
* Automatically bump versions based on **Semantic Versioning (SemVer)** rules.
* Generate and maintain `CHANGELOG.md` autonomously.
* Draft and publish official GitHub Releases.

### 4. Deployment Control (CD) & Environments
The Deployment pipeline (`deploy.yml`) handles artifact creation and promotion:
* **Staging:** Automated build and deployment upon package release.
* **Production (`prod`):** Guarded by a **Manual Approval Gate** requiring explicit Release Manager sign-off within GitHub Environments.

---

## Operations Guide (Runbook)

### Executing a Routine Release
1. Open a feature branch and commit changes using prefixes (e.g., `feat: login endpoint`).
2. Open a PR, verify CI passes, and execute a **Squash and Merge**.
3. Locate the automated release PR created by `github-actions[bot]`, review the changelog, and merge it.

### Executing an Emergency Rollback
In the event of a production failure:
1. Navigate to **Actions** -> **Continuous Deployment**.
2. Click **Run workflow**.
3. Input the last known stable tag (e.g., `v0.3.0`) into the `rollback_version` field.
4. Approve the deployment gate to force immediate rollback deployment.

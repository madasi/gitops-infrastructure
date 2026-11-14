# Branch Naming Convention

Use a short prefix to describe the primary kind of work, followed by a lowercase, kebab-case summary:

```text
<type>/<short-description>
```

Examples:

| Prefix | Use for | Example |
| --- | --- | --- |
| `feat/` | New functionality | `feat/tailscale-subnet-router` |
| `fix/` | Bug fixes | `fix/ansible-dns-record-update` |
| `refactor/` | Restructuring without intended behavior changes | `refactor/ansible-roles` |
| `ci/` | CI/CD workflows and automation | `ci/github-actions-baseline` |
| `docs/` | Documentation, journal entries, and other written guidance | `docs/journal-2026-11-14` |
| `chore/` | Maintenance, dependency updates, and repository housekeeping | `chore/update-ansible-collections` |

Choose the prefix that best describes the branch's main purpose. Keep descriptions concise and specific. These prefixes are a lightweight naming convention, not a substitute for reviewing the changes in a pull request.

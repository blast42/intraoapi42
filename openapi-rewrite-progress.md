# OpenAPI Rewrite Progress — Intra 42 API

Tracking progress of rewriting the legacy Intra 42 API documentation into a proper OpenAPI 3.1 spec.

## Legend

| Status | Meaning |
|---|---|
| ✅ Done | Schema + operation fully written, tested against a real response |
| 🚧 In progress | Created but not fully tested / needs review |
| ❌ Impossible | Endpoint doesn't return anything, is deprecated, or can't be verified |
| ⏳ To do | Not started yet |
| ⚠️ Blocked | Waiting on missing info (enum values, unclear fields, access rights) |

---

## Accreditations

| Method | Path | Status | Notes |
|---|---|---|---|
| Accreditations |
| GET | `/accreditations` | 🚧 In progress | |
| GET | `/accreditations/{id}` | 🚧 In progress | |
| POST | `/accreditations` | ⏳ To do | |
| PATCH | `/accreditations/{id}` | ⏳ To do | |
| PUT | `/accreditations/{id}` | ⏳ To do | |
| DELETE | `/accreditations/{id}` | ⏳ To do | |
| Achievements |
| GET | `/achievements` | ⏳ To do | |
| GET | `/cursus/{cursus_id}/achievements` | ⏳ To do | |
| GET | `/campus/{campus_id}/achievements` | ⏳ To do | |
| GET | `/titles/{title_id}/achievements` | ⏳ To do | |
| GET | `/achievements/{id}` | ⏳ To do | |
| POST | `/achievements` | ⏳ To do | |
| PATCH | `/achievements/{id}` | ⏳ To do | |
| PUT | `/achievements/{id}` | ⏳ To do | |
| DELETE | `/achievements/{id}` | ⏳ To do | |
| Achievements users |

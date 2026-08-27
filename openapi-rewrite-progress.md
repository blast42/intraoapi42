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
| GET | `/accreditations` | 🚧 In progress | |
| GET | `/accreditations/{id}` | 🚧 In progress | |
| POST | `/accreditations` | ⏳ To do | |
| PATCH | `/accreditations/{id}` | ⏳ To do | |
| PUT | `/accreditations/{id}` | ⏳ To do | |
| DELETE | `/accreditations/{id}` | ⏳ To do | |

## Achievements

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/achievements` | ⏳ To do | |
| GET | `/cursus/{cursus_id}/achievements` | ⏳ To do | |
| GET | `/campus/{campus_id}/achievements` | ⏳ To do | |
| GET | `/titles/{title_id}/achievements` | ⏳ To do | |
| GET | `/achievements/{id}` | ⏳ To do | |
| POST | `/achievements` | ⏳ To do | |
| PATCH | `/achievements/{id}` | ⏳ To do | |
| PUT | `/achievements/{id}` | ⏳ To do | |
| DELETE | `/achievements/{id}` | ⏳ To do | |

## Achievements users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/achievements/{achievement_id}/achievements_users` | ⏳ To do | |
| GET | `/achievements_users` | ⏳ To do | |
| GET | `/achievements_users/{id}` | ⏳ To do | |
| POST | `/achievements_users` | ⏳ To do | |
| PATCH | `/achievements_users/{id}` | ⏳ To do | |
| PUT | `/achievements_users/{id}` | ⏳ To do | |
| DELETE | `/achievements_users/{id}` | ⏳ To do | |

## Alumnized users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/alumnized_users` | ⏳ To do | |

## Amendments

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/amendments` | ⏳ To do | |
| GET | `/users/{user_id}/amendments` | ⏳ To do | |
| GET | `/internships/{internship_id}/amendments` | ⏳ To do | |
| GET | `/amendments/{id}` | ⏳ To do | |
| POST | `/amendments` | ⏳ To do | |
| DELETE  | `/amendments/{id}` | ⏳ To do | |

## Announcements

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/announcements/{id}` | ⏳ To do | |
| POST | `/announcements` | ⏳ To do | |
| POST | `/cursus/{cursus_id}/announcements` | ⏳ To do | |
| PATCH | `/announcements/{id}` | ⏳ To do | |
| PUT | `/announcements/{id}` | ⏳ To do | |
| DELETE | `/announcements/{id}` | ⏳ To do | |

## Anti grav units

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/anti_grav_units` | ⏳ To do | |
| GET | `/anti_grav_units/{id}` | ⏳ To do | |

## Anti grav units users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/anti_grav_units_users` | ⏳ To do | |
| GET | `/users/{user_id}/anti_grav_units_users` | ⏳ To do | |

## Closes

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/closes` | 🚧 In progress | |
| GET | `/closes/{id}` | 🚧 In progress | |
| GET | `/users/{user_id}/closes` | 🚧 In progress | |

## Internships

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/internships` | 🚧 In progress | |
| GET | `/internships/{id}` | 🚧 In progress | |
| GET | `/users/{user_id}/internships` | 🚧 In progress | |
| GET | `/users/{user_id}/internships/{id}` | 🚧 In progress | |

## Languages

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/languages/{id}` | 🚧 In progress | |


## Project sessions

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/project_sessions/{project_session_id}/teams` | 🚧 In progress | |

## Projects

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/projects/{project_id}/projects_users` | 🚧 In progress | |
| GET | `/projects/{project_id}/teams` | 🚧 In progress | |

## Projects users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/projects_users` | 🚧 In progress | |
| GET | `/projects_users/{id}` | 🚧 In progress | |
| POST | `/projects_users` | 🚧 In progress | |
| PATCH | `/projects_users/{id}` | 🚧 In progress | |
| PUT | `/projects_users/{id}` | 🚧 In progress | |
| GET | `/users/{user_id}/projects_users` | 🚧 In progress | |

## Teams

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/teams` | 🚧 In progress | |
| GET | `/me/teams` | 🚧 In progress | |
| GET | `/teams/{id}` | 🚧 In progress | |
| PATCH | `/teams/{id}` | 🚧 In progress | |
| PUT | `/teams/{id}` | 🚧 In progress | |
| POST | `/teams/{id}/reset_team_uploads` | 🚧 In progress | |
| GET | `/users/{user_id}/teams` | 🚧 In progress | |
| GET | `/users/{user_id}/projects/{project_id}/teams` | 🚧 In progress | |
| GET | `/projects/{project_id}/teams` | 🚧 In progress | |

## Users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/users` | 🚧 In progress | |
| GET | `/users/{id}/user_candidature` | 🚧 In progress | |
| GET | `/achievements/{achievement_id}/users` | 🚧 In progress | |
| GET | `/accreditations/{accreditation_id}/users` | 🚧 In progress | |
| GET | `/achievements/{achievement_id}/users` | 🚧 In progress | |
| GET | `/titles/{title_id}/users` | 🚧 In progress | |
| GET | `/quests/{quest_id}/users` | 🚧 In progress | |
| GET | `/projects/{project_id}/users` | 🚧 In progress | |
| GET | `/partnerships/{partnership_id}/users` | 🚧 In progress | |
| GET | `/expertises/{expertise_id}/users` | 🚧 In progress | |
| GET | `/cursus/{cursus_id}/users` | 🚧 In progress | |
| GET | `/coalitions/{coalition_id}/users` | 🚧 In progress | |
| GET | `/campus/{campus_id}/users` | 🚧 In progress | |
| GET | `/users/{id}` | 🚧 In progress | |
| GET | `/me` | ⏳ To do | |


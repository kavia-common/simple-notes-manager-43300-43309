# simple-notes-manager-43300-43309

## Simple Notes API

This backend provides a CRUD REST API for notes.

### Endpoints

All endpoints are prefixed by `/api/notes/` for notes resources.

#### List notes (paginated by 10, ordered by updated_at desc)
```bash
curl -X GET http://localhost:3001/api/notes/
```

#### Create a new note
```bash
curl -X POST http://localhost:3001/api/notes/ -H "Content-Type: application/json" -d '{"title": "My title", "content": "Hello world!"}'
```

#### Retrieve a note by ID
```bash
curl -X GET http://localhost:3001/api/notes/1/
```

#### Update an existing note
```bash
curl -X PUT http://localhost:3001/api/notes/1/ -H "Content-Type: application/json" -d '{"title": "Updated", "content": "Updated text."}'
```

#### Partially update a note
```bash
curl -X PATCH http://localhost:3001/api/notes/1/ -H "Content-Type: application/json" -d '{"content": "Partial update only."}'
```

#### Delete a note
```bash
curl -X DELETE http://localhost:3001/api/notes/1/
```

## Health Check
```bash
curl -X GET http://localhost:3001/api/health/
```

## API doc
Browse [http://localhost:3001/docs/](http://localhost:3001/docs/) for live OpenAPI docs.

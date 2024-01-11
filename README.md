AirBnB_clone
----
Repository contain:
1. The console
2. Data model
The repository will:
1. Manage (create, update, destroy, etc) objects via a console / command interpreter
2. Store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow me to change the type of storage easily without updating all of my codebase.

The console is a tool to validate this storage engine


db.createUser({
    user: "jira_user",
    pwd: "jira_password",
    roles: [
        {
            role: "readWrite",
            db: "jira_backup"
        }
    ]
});


db.createCollection('users');
db.createCollection('issues');
db.createCollection('attachments');
db.createCollection('worklogs');



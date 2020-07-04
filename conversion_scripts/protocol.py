def define_new_protocol(REPRONIM_REPO, REMOTE_REPO, BRANCH, protocol, VERSION):
    # define the jsonld for the schema protocol

    protocol["schema_file"] = protocol["name"] + "schema"
    protocol["context_file"] = protocol["name"] + "context"
    protocol["dir"] = protocol["name"][0:-1]

    protocol["schema"] = {
        "@context": [
            REPRONIM_REPO + "contexts/generic",
            REMOTE_REPO
            + BRANCH
            + "/protocols/"
            + protocol["dir"]
            + "/"
            + protocol["context_file"],
        ],
        "@type": "reproschema:Protocol",
        "@id": protocol["schema_file"],
        "prefLabel": protocol["schema_file"],
        "schema:description": protocol["schema_file"],
        "schema:schemaVersion": VERSION,
        "schema:version": VERSION,
        "landingPage": REMOTE_REPO
        + BRANCH
        + "/protocols/"
        + protocol["dir"]
        + "/README.md",
        "ui": {
            "allow": ["autoAdvance", "allowExport"],
            "shuffle": False,
            "order": [],
            "addProperties": [],
        },
    }

    # define the jsonld for the context associated to this protocol
    protocol["context"] = {
        "@context": {
            "@version": 1.1,
            "activity_path": REMOTE_REPO + BRANCH + "/activities/",
        }
    }

    return protocol


def update_protocol(activity, protocol):

    # update the content of the protool schema and context wrt this new activity
    append_to_protocol = {
        "variableName": activity["name"],
        "isAbout": activity["name"],
        # for the name displayed by the UI for this activity we simply reuse the
        # activity name
        "prefLabel": {"en": activity["pref_label"]},
    }

    protocol["schema"]["ui"]["order"].append(activity["name"])
    protocol["schema"]["ui"]["addProperties"].append(append_to_protocol)

    protocol["context"]["@context"][activity["name"]] = {
        "@id": "activity_path:" + activity["name"] + "/" + activity["schema_file"],
        "@type": "@id",
    }

    return protocol

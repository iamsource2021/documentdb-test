# documentdb-test
## Creating a Graphql API for AWS DocumentDB and MongoDB Atlas with AWS Amplify




CRUD generated with amplify-cli with a graphql api, resolvers with lambda functions, python 3.8 runtime and non-relational database storage, mongodb, serverless

## Features

- python_version = "3.8"
- pymongo = {version = "==4.0.1", extras = ["srv"]}
- python-dotenv = "==0.19.2"
- dnspython = "==2.2.0"
- AWS Lambda
- AWS DocumentDB
- AWS Amplify
- AWS Appsync
- MongoDB Atlas cluster
- GraphQL API
- pattern design: Observer, Resolvers
- Microservices

## Installation

documentdb-test requires [AWS Amplify](https://docs.amplify.aws/start/getting-started/installation/q/integration/js/) to run.

Install the dependencies and devDependencies and start the requirements.txt.

```sh
pipenv install -r requirements.txt
```

For production environments AWS amplify.

```sh
amplify push
```

## Development

uses amplify mock function.

```sh
amplify mock function myFunctionName
```
uses amplify mock api.

```sh
amplify mock api
```

Schema GrapQL amplify/backend/api/documentdbtest/schema.graphql

```sh
# This "input" configures a global authorization rule to enable public access to
# all models in this schema. Learn more about authorization rules here: https://docs.amplify.aws/cli/graphql/authorization-rules
input AMPLIFY { globalAuthRule: AuthRule = { allow: public } } # FOR TESTING ONLY!

type Profile {
  nombre: String
  razonsocial: String
  rfc: String
  direccion: String
  telefono:String
}

input createProfileInput {
  nombre: String
  razonsocial: String
  rfc: String!
  direccion: String
  telefono:String
}

input updateProfileInput {
  nombre: String
  razonsocial: String
  rfc: String!
  direccion: String
  telefono:String
}

input deleteProfileInput {
  rfc: String
}

type Query {
  listProfile: [Profile]
    @function(name: "documentdbtest3b411186-${env}")
  getProfile(rfc: String!):  Profile
    @function(name: "documentdbtest2ece4974-${env}")
}

type Mutation {
  createProfile(input:createProfileInput):Profile
    @function(name: "documentdbtest76d3ab8a-${env}")
  updateProfile(input:updateProfileInput):Profile
    @function(name: "documentdbtest7066ed43-${env}")
  deleteProfile(input:deleteProfileInput):Profile
    @function(name: "documentdbtestc9062471-${env}")        
}

type Subscription {
  onCreateProfile:Profile
    @aws_subscribe(mutations: ["createProfile"])
  onUpdateProfile:Profile
    @aws_subscribe(mutations: ["updateProfile"])
  onDeleteProfile:Profile
    @aws_subscribe(mutations: ["deleteProfile"])     
}
```

python code with lambda functions

listProfile

```sh
amplify/backend/function/documentdbtest3b411186
```

getProfile

```sh
amplify/backend/function/documentdbtest2ece4974
```

createProfile

```sh
amplify/backend/function/documentdbtest76d3ab8a
```

updateProfile

```sh
amplify/backend/function/documentdbtest7066ed43
```

deleteProfile

```sh
amplify/backend/function/documentdbtestc9062471
```

## API Docs

Query.listProfile: [Profile] - customer list
```sh
    query listProfile {
      listProfile {
        direccion
        nombre
        razonsocial
        rfc
        telefono
      }
    }
    
    response:
    
    {
  "data": {
    "listProfile": [
      {
        "direccion": "Montes Urales # 445, en la Ciudad de México",
        "nombre": "Matt Ramirez",
        "razonsocial": "Google en México",
        "rfc": "GOM0809114P5",
        "telefono": "522299897300"
      },
      {
        "direccion": "Montes Urales # 445, en la Ciudad de México",
        "nombre": "Frank Ortega",
        "razonsocial": "Google en México",
        "rfc": "GOM0809114P6",
        "telefono": "53428400"
      },
      {
        "direccion": "Montes Urales # 445, en la Ciudad de México",
        "nombre": "Karen Lopez",
        "razonsocial": "Google en México",
        "rfc": "GOM0809114P7",
        "telefono": "53428400"
      },
      {
        "direccion": "Montes Urales # 445, en la Ciudad de México",
        "nombre": "Karen Lopez",
        "razonsocial": "Google en México",
        "rfc": "GOM0809114P8",
        "telefono": "53428400"
      }
    ]
  }
}
```

Query.getProfile(rfc: String!):  Profile - one customer
```sh
query getProfile {
  getProfile(rfc: "53428400") {
    direccion
    nombre
    razonsocial
    rfc
    telefono
  }
}

 response:
 
{
  "data": {
    "getProfile": {
      "direccion": "Montes Urales # 445, en la Ciudad de México",
      "nombre": "Karen Lopez",
      "razonsocial": "Google en México",
      "rfc": "GOM0809114P8",
      "telefono": "53428400"
    }
  }
}
```



Mutation.createProfile(input:createProfileInput):Profile - create customer
```sh
mutation createProfile {
  createProfile(
    input: {
      direccion: "Montes Urales # 445, en la Ciudad de México"
      nombre: "Karen Lopez"
      razonsocial: "Google en México"
      rfc: "GOM0809114P8"
      telefono: "53428400"
    }
  ) {
    direccion
    nombre
    razonsocial
    rfc
    telefono
  }
}

 response:
 
 {
  "data": {
    "createProfile": {
      "direccion": "Montes Urales # 445, en la Ciudad de México",
      "nombre": "Karen Lopez",
      "razonsocial": "Google en México",
      "rfc": "GOM0809114P8",
      "telefono": "53428400"
    }
  }
}
```
Mutation.updateProfile(input:updateProfileInput):Profile - update customer
```sh
subscription onCreateProfile {
  onCreateProfile {
    direccion
    nombre
    razonsocial
    rfc
    telefono
  }
}
```

Mutation.deleteProfile(input:deleteProfileInput):Profile  - delete customer
```sh
subscription onCreateProfile {
  onCreateProfile {
    direccion
    nombre
    razonsocial
    rfc
    telefono
  }
}
```

Subscription.onCreateProfile:Profile - trigger create customer
```sh
subscription onCreateProfile {
  onCreateProfile {
    direccion
    nombre
    razonsocial
    rfc
    telefono
  }
}
```

Subscription.onUpdateProfile:Profile - trigger update customer   
```sh
subscription onUpdateProfile  {
  onCreateProfile {
    direccion
    nombre
    razonsocial
    rfc
    telefono
  }
}
```

Subscription.onDeleteProfile:Profile - trigger delete customer 
```sh
subscription onDeleteProfile {
  onCreateProfile {
    direccion
    nombre
    razonsocial
    rfc
    telefono
  }
}
```


## License

MIT


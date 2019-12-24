pipeline {
    agent any 
    stages {
        stage('push') { 
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'Mahesh_Credential', url: 'https://github.com/MaheshGavandar/Python.git']]])
            }
        }
    }
}

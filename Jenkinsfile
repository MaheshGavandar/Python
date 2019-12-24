pipeline {
    agent any 
    stages {
        stage('push') { 
            steps {
                git credentialsId: 'Mahesh_Credential', url: 'https://github.com/MaheshGavandar/Python.git, branch: develop'

                    sh 'git tag -a tagName -m "Your tag comment"'
                    sh 'git merge develop'
                    sh 'git commit -am "Merged develop branch to master'
                    sh "git push origin master
            }
        }
    }
}

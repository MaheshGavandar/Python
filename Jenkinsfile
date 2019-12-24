pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
              sh('echo \$BUILD_NUMBER > example-\$BUILD_NUMBER.md')
            }
        }
        stage('commit') { 
            steps {
                sh('''
                    git checkout -B $TARGET_BRANCH
                    git add . && git commit -am "[Jenkins CI] Add build file"
                ''')
            }
        }
        stage('push') { 
            environment { 
                GIT_AUTH = credentials('Mahesh_Credential') 
            }
            steps {
                sh('''
                    git config --local credential.helper "!f() { echo username=\\$Username; echo password=\\$Password; }; f"
                    git push origin HEAD:$TARGET_BRANCH
                ''')
            }
        }
    }
}

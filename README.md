# github-actions-python

my-python-api/
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── .github/
    └── workflows/
        └── deploy.yaml

mkdir -p ~/github-runners/python-api-runner
cd ~/github-runners/python-api-runner

curl -LO https://github.com/actions/runner/releases/download/v2.316.0/actions-runner-linux-x64-2.316.0.tar.gz
tar xzf actions-runner-linux-x64-2.316.0.tar.gz

./config.sh --url https://github.com/fredwinrosales/github-actions-python --token <TOKEN> --name python-runner --labels self-hosted,python

sudo ./svc.sh install

sudo ./svc.sh start

sudo systemctl status actions.runner.fredwinrosales-github-actions-python.*

systemctl list-units | grep actions.runner

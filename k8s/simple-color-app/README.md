sudo apt update -y
sudo apt install python3-pip -y
pip3 install flask

python3 -m venv myenv
source myenv/bin/activate

kind load docker-image color-app:v1.0.1 --name kind-cluster
kubectl set image deployment/my-app app=my-app:v2
kubectl rollout restart deployment/my-app

kubectl port-forward service/myapp-service 8080:80

# Watch rollout status
kubectl rollout status deployment/my-app

# View rollout history
kubectl rollout history deployment/my-app

# See details of a specific revision
kubectl rollout history deployment/my-app --revision=2

# Undo to previous version
kubectl rollout undo deployment/my-app

# Rollback to specific revision
kubectl rollout undo deployment/my-app --to-revision=3
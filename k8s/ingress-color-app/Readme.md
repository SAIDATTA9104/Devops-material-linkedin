docker run -p 5000:5000 -e BG_COLOR="coral" color-app
kind load docker-image blue-app:v1.0.0 --name kind-cluster

kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.7/config/manifests/metallb-native.yaml

# Check services
kubectl get svc

# Check ingress
kubectl get ingress

# View logs
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx

kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80

# Kubernetes Multi-Container Application

This directory contains Kubernetes manifests to deploy the multi-container application that was previously defined using Docker Compose.

## Components

- **Frontend**: A simple web interface served by Nginx
- **Backend**: A Flask API that provides time information
- **Redis**: Used for caching time information
- **Ingress**: Routes traffic to the appropriate services based on path

## Kubernetes Resources

- **Deployments**: Define the containers to run
- **Services**: Expose the deployments within the cluster
- **Ingress**: Exposes the services to external traffic
- **Secret**: Stores sensitive information (Redis password)
- **ConfigMap**: Stores configuration data
- **Namespace**: Organizes all resources

## Deployment Instructions

1. Create the namespace:
   ```
   kubectl apply -f namespace.yaml
   ```

2. Create the secret:
   ```
   kubectl apply -f redis-secret.yaml
   ```

3. Create the ConfigMap:
   ```
   kubectl apply -f configmap.yaml
   ```

4. Deploy Redis:
   ```
   kubectl apply -f redis-deployment.yaml
   kubectl apply -f redis-service.yaml
   ```

5. Deploy the backend:
   ```
   kubectl apply -f backend-deployment.yaml
   kubectl apply -f backend-service.yaml
   ```

6. Deploy the frontend:
   ```
   kubectl apply -f frontend-deployment.yaml
   kubectl apply -f frontend-service.yaml
   ```

7. Create the Ingress:
   ```
   kubectl apply -f ingress.yaml
   ```

8. Access the application:
   ```
   http://localhost/
   ```

## Notes

- This assumes that you have a Kubernetes cluster with an Ingress controller installed
- The container images are assumed to be available in a registry (referenced as `frontend:latest` and `backend:latest`)
- For a real production deployment, you would want to use specific image tags rather than `latest`

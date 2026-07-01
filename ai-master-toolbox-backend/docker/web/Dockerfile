FROM node:18 as DIST
WORKDIR /app
COPY ./ai-master-toolbox-frontend .
RUN npm install \
    && npm run build

FROM nginx:latest
COPY ./ai-master-toolbox-backend/docker/web/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=DIST /app/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]




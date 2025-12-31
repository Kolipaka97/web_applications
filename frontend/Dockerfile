FROM nginx:alpine
RUN adduser -D appuser

COPY index.html /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf

USER appuser
EXPOSE 80

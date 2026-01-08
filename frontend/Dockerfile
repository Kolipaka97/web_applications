FROM nginx:alpine

# Copy your frontend build files
COPY build/ /usr/share/nginx/html/

# Copy custom nginx config if you have one
COPY nginx.conf /etc/nginx/nginx.conf

# Create cache folder and give nginx permission
RUN mkdir -p /var/cache/nginx/client_temp && \
    chown -R nginx:nginx /var/cache/nginx

# Expose port
EXPOSE 80

# Run nginx as non-root
USER nginx

CMD ["nginx", "-g", "daemon off;"]

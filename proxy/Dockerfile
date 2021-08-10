FROM nginx

RUN apt-get update && apt-get install -y --no-install-recommends \
		nano   \
	  && rm -rf /var/lib/apt/lists/*


#COPY index.html /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/*

COPY proxy.conf /etc/nginx/conf.d/




FROM ubuntu:22.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Update and install basic utilities
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    apt-utils \
    build-essential \
    curl \
    git \
    wget \
    software-properties-common \
    openssh-server \
    sudo \
    nano \
    net-tools \
    iputils-ping \
    ca-certificates

RUN apt-get install ldap-utils
COPY ldap.conf /etc/ldap.conf
COPY ldap.conf /etc/ldap/ldap.conf

RUN apt-get install -y libnss-ldap
RUN apt-get install -y libpam-ldap

COPY nsswitch.conf /etc/nsswitch.conf
COPY common-auth /etc/pam.d/common-auth
COPY common-account /etc/pam.d/common-account
COPY common-session /etc/pam.d/common-session
COPY common-passwd /etc/pam.d/common-passwd

RUN dpkg-reconfigure ldap-auth-config

RUN apt-get install -y vsftpd

# Configure vsftpd to run in the foreground
RUN sed -i 's/listen=NO/listen=YES/' /etc/vsftpd.conf && \
    sed -i 's/listen_ipv6=YES/listen_ipv6=NO/' /etc/vsftpd.conf

RUN echo "local_enable=YES" >> /etc/vsftpd.conf
RUN echo "write_enable=YES"  >> /etc/vsftpd.conf
RUN echo "chroot_local_user=YES"  >> /etc/vsftpd.conf
RUN echo "allow_writeable_chroot=YES"  >> /etc/vsftpd.conf
    

RUN mkdir /home/users
RUN mkdir -p /var/run/vsftpd/empty
RUN chmod 555 /var/run/vsftpd/empty

# Create volume mount point
VOLUME ["/home/users"]

# Create an entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 21

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
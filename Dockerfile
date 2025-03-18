FROM alpine:latest

RUN apk add alpine-sdk alpine-conf syslinux xorriso squashfs-tools grub grub-efi mtools dosfstools doas openssh

RUN adduser -G abuild -s /bin/sh -D build
RUN echo "permit persist :abuild" > /etc/doas.d/doas.conf
WORKDIR /src

RUN abuild-keygen -a -n
RUN git clone --depth=1 https://gitlab.alpinelinux.org/alpine/aports.git

RUN apk add libvirt-daemon qemu-img qemu-system-x86_64 qemu-modules openrc virt-install libvirt dbus polkit openvswitch openssh

ADD mkimg.nightlight.sh /src/aports/scripts
ADD genapkovl-mkimgnightlight.sh /src/aports/scripts
ADD tui/menu.py /src/aports/scripts

RUN chmod +x /src/aports/scripts/genapkovl-mkimgnightlight.sh
RUN apk update

CMD sh aports/scripts/mkimage.sh --outdir /build --tag main --arch x86_64 --repository https://dl-cdn.alpinelinux.org/alpine/v3.21/main --repository https://dl-cdn.alpinelinux.org/alpine/v3.21/community --profile nightlight

profile_nightlight() {
        profile_standard
	boot_addons="amd-ucode intel-ucode"
	initrd_ucode="/boot/amd-ucode.img /boot/intel-ucode.img"
        apks="$apks openvswitch libvirt-daemon qemu-img qemu-system-x86_64 qemu-modules openrc virt-install libvirt dbus polkit
                cciss_vol_status lvm2 mdadm mkinitfs mtools nfs-utils
                parted rsync sfdisk syslinux util-linux xfsprogs
                dosfstools ntfs-3g
                "
        local _k _a
        for _k in $kernel_flavors; do
                apks="$apks linux-$_k"
                for _a in $kernel_addons; do
                        apks="$apks $_a-$_k"
                done
        done
        apks="$apks linux-firmware"
        apkovl="aports/scripts/genapkovl-mkimgnightlight.sh"
}

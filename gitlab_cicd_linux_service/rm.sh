svc="service"

systemctl daemon-reload
systemctl stop $svc.service
systemctl disable $svc.service
svc="service"

systemctl daemon-reload
systemctl start $svc.service
systemctl enable $svc.service
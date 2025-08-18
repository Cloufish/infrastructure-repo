
## TAKEAWAYS
- etcd is setup on each control plane node, so unavailability on first node shouldn't be an issue
- HAPRoxy doesn't require SSL Certificates for Kubernetes API calls however, Kubernetes uses its own keys to authenticate to the API
- kube-apiserver turns off probably because of etcd not available
- etcd performs a normal shutdown process
- when kube-apiserver turns off, other components also turn off
- The first containers to stop working is kube-proxy and kube-scheduler. But is it possible that

## LOGS
ubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ for more information.
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: Flag --pod-infra-container-image has been deprecated, will be removed in a future release. Image garbage collector will get sandbox image information from CRI.
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.636596     906 server.go:211] "--pod-infra-container-image will not be pruned by the image garbage collector in kubelet and should also be set in the remote runtime"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.641178     906 server.go:491] "Kubelet version" kubeletVersion="v1.31.9"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.641197     906 server.go:493] "Golang settings" GOGC="" GOMAXPROCS="" GOTRACEBACK=""
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.641457     906 server.go:934] "Client rotation is on, will bootstrap in background"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.642716     906 certificate_store.go:130] Loading cert/key pair from "/var/lib/kubelet/pki/kubelet-client-current.pem".
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.644531     906 dynamic_cafile_content.go:160] "Starting controller" name="client-ca-bundle::/etc/kubernetes/pki/ca.crt"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: E0615 18:07:04.657891     906 log.go:32] "RuntimeConfig from runtime service failed" err="rpc error: code = Unimplemented desc = unknown method RuntimeConfig for service runtime.v1.RuntimeService"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.657921     906 server.go:1408] "CRI implementation should be updated to support RuntimeConfig when KubeletCgroupDriverFromCRI feature gate has been enabled. Falling back to using cgroupDriver from kubelet config."
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.662750     906 server.go:749] "--cgroups-per-qos enabled, but --cgroup-root was not specified.  defaulting to /"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.663336     906 swap_util.go:113] "Swap is on" /proc/swaps contents="Filename\t\t\t\tType\t\tSize\t\tUsed\t\tPriority"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.663544     906 container_manager_linux.go:264] "Container manager verified user specified cgroup-root exists" cgroupRoot=[]
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.663574     906 container_manager_linux.go:269] "Creating Container Manager object based on Node Config" nodeConfig={"NodeName":"k8s-control-plane-2","RuntimeCgroupsName":"","SystemCgroupsName":"","KubeletCgroupsName":"","KubeletOOMScoreAdj":-999,"ContainerRuntime":"","CgroupsPerQOS":true,"CgroupRoot":"/","CgroupDriver":"systemd","KubeletRootDir":"/var/lib/kubelet","ProtectKernelDefaults":false,"KubeReservedCgroupName":"","SystemReservedCgroupName":"","ReservedSystemCPUs":{},"EnforceNodeAllocatable":{"pods":{}},"KubeReserved":null,"SystemReserved":null,"HardEvictionThresholds":[{"Signal":"memory.available","Operator":"LessThan","Value":{"Quantity":"100Mi","Percentage":0},"GracePeriod":0,"MinReclaim":null},{"Signal":"nodefs.available","Operator":"LessThan","Value":{"Quantity":null,"Percentage":0.1},"GracePeriod":0,"MinReclaim":null},{"Signal":"nodefs.inodesFree","Operator":"LessThan","Value":{"Quantity":null,"Percentage":0.05},"GracePeriod":0,"MinReclaim":null},{"Signal":"imagefs.available","Operator":"LessThan","Value":{"Quantity":null,"Percentage":0.15},"GracePeriod":0,"MinReclaim":null},{"Signal":"imagefs.inodesFree","Operator":"LessThan","Value":{"Quantity":null,"Percentage":0.05},"GracePeriod":0,"MinReclaim":null}],"QOSReserved":{},"CPUManagerPolicy":"none","CPUManagerPolicyOptions":null,"TopologyManagerScope":"container","CPUManagerReconcilePeriod":10000000000,"ExperimentalMemoryManagerPolicy":"None","ExperimentalMemoryManagerReservedMemory":null,"PodPidsLimit":-1,"EnforceCPULimits":true,"CPUCFSQuotaPeriod":100000000,"TopologyManagerPolicy":"none","TopologyManagerPolicyOptions":null,"CgroupVersion":2}
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.664434     906 topology_manager.go:138] "Creating topology manager with none policy"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.664457     906 container_manager_linux.go:300] "Creating device plugin manager"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.665008     906 state_mem.go:36] "Initialized new in-memory state store"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.669033     906 kubelet.go:408] "Attempting to sync node with API server"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.669059     906 kubelet.go:303] "Adding static pod path" path="/etc/kubernetes/manifests"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.669082     906 kubelet.go:314] "Adding apiserver pod source"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.669735     906 apiserver.go:42] "Waiting for node sync before watching apiserver pods"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.677030     906 kuberuntime_manager.go:262] "Container runtime initialized" containerRuntime="containerd" version="1.7.27" apiVersion="v1"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.680351     906 kubelet.go:837] "Not starting ClusterTrustBundle informer because we are in static kubelet mode"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.682711     906 server.go:1274] "Started kubelet"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.687264     906 ratelimit.go:55] "Setting rate limiting for endpoint" service="podresources" qps=100 burstTokens=10
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.688271     906 server.go:236] "Starting to serve the podresources API" endpoint="unix:/var/lib/kubelet/pod-resources/kubelet.sock"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.688417     906 server.go:163] "Starting to listen" address="0.0.0.0" port=10250
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.688881     906 fs_resource_analyzer.go:67] "Starting FS ResourceAnalyzer"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.689850     906 server.go:449] "Adding debug handlers to kubelet server"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.691890     906 scope.go:117] "RemoveContainer" containerID="75e8775dbfbb70edb60648b2c61ef4d270771c566aeb4e7b1d2ba577dbb84ab4"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: E0615 18:07:04.697205     906 kubelet.go:1478] "Image garbage collection failed once. Stats initialization may not have completed yet" err="invalid capacity 0 on image filesystem"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.702980     906 dynamic_serving_content.go:135] "Starting controller" name="kubelet-server-cert-files::/var/lib/kubelet/pki/kubelet.crt::/var/lib/kubelet/pki/kubelet.key"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.705726     906 volume_manager.go:289] "Starting Kubelet Volume Manager"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: E0615 18:07:04.706472     906 kubelet_node_status.go:453] "Error getting the current node from lister" err="node \"k8s-control-plane-2\" not found"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: I0615 18:07:04.707461     906 desired_state_of_world_populator.go:147] "Desired state populator starts to run"
Jun 15 18:07:04 k8s-control-plane-2 kubelet[906]: E0615 18:07:04.709299     906 event.go:368] "Unable to write event (may retry after sleeping)" err="Post \"https://192.168.1.160:6443/api/v1/namespaces/default/events\": EOF" event="&Event{ObjectMeta:{k8s-control-plane-2.1849430654db9956  default    0 0001-01-01 00:00:00 +0000 UTC <nil> <nil> map[] map[] [] [] []},InvolvedObject:ObjectReference{Kind:Node,Namespace:

## kube-proxy and kube-scheduler verification

Seems like the error is in kube-proxy and kube-scheduler. It fails first on all nodes

```
 sudo crictl logs 432 (kube-proxy)
 
I0615 19:52:22.228545       1 server_linux.go:63] "Using iptables proxy"
I0615 19:52:22.380580       1 server.go:715] "Successfully retrieved node IP(s)" IPs=["192.168.1.161"]
I0615 19:52:22.387485       1 conntrack.go:60] "Setting nf_conntrack_max" nfConntrackMax=131072
E0615 19:52:22.387817       1 server.go:245] "Kube-proxy configuration may be incomplete or incorrect" err="nodePortAddresses is unset; NodePort connections will be accepted on all local IPs. Consider using `--nodeport-addresses primary`"
I0615 19:52:22.470117       1 server.go:254] "kube-proxy running in dual-stack mode" primary ipFamily="IPv4"
I0615 19:52:22.470256       1 server_linux.go:145] "Using iptables Proxier"
I0615 19:52:22.500934       1 proxier.go:243] "Setting route_localnet=1 to allow node-ports on localhost; to change this either disable iptables.localhostNodePorts (--iptables-localhost-nodeports) or set nodePortAddresses (--nodeport-addresses) to filter loopback addresses" ipFamily="IPv4"
I0615 19:52:22.502294       1 server.go:516] "Version info" version="v1.33.1"
I0615 19:52:22.502450       1 server.go:518] "Golang settings" GOGC="" GOMAXPROCS="" GOTRACEBACK=""
I0615 19:52:22.517563       1 config.go:199] "Starting service config controller"
I0615 19:52:22.517996       1 shared_informer.go:350] "Waiting for caches to sync" controller="service config"
I0615 19:52:22.520296       1 config.go:105] "Starting endpoint slice config controller"
I0615 19:52:22.521017       1 shared_informer.go:350] "Waiting for caches to sync" controller="endpoint slice config"
I0615 19:52:22.521426       1 config.go:440] "Starting serviceCIDR config controller"
I0615 19:52:22.521830       1 shared_informer.go:350] "Waiting for caches to sync" controller="serviceCIDR config"
I0615 19:52:22.522847       1 config.go:329] "Starting node config controller"
I0615 19:52:22.522936       1 shared_informer.go:350] "Waiting for caches to sync" controller="node config"
I0615 19:52:22.618528       1 shared_informer.go:357] "Caches are synced" controller="service config"
I0615 19:52:22.622135       1 shared_informer.go:357] "Caches are synced" controller="endpoint slice config"
I0615 19:52:22.622559       1 shared_informer.go:357] "Caches are synced" controller="serviceCIDR config"
I0615 19:52:22.623331       1 shared_informer.go:357] "Caches are synced" controller="node config"
```

```
 sudo crictl logs 15c (kube-scheduler)
I0615 20:01:20.660534       1 serving.go:386] Generated self-signed cert in-memory
W0615 20:01:21.980206       1 authentication.go:397] Error looking up in-cluster authentication configuration: Get "https://192.168.1.161:6443/api/v1/namespaces/kube-system/configmaps/extension-apiserver-authentication": dial tcp 192.168.1.161:6443: connect: connection refused
W0615 20:01:21.980293       1 authentication.go:398] Continuing without authentication configuration. This may treat all requests as anonymous.
W0615 20:01:21.980321       1 authentication.go:399] To require authentication configuration lookup to succeed, set --authentication-tolerate-lookup-failure=false
I0615 20:01:22.005946       1 server.go:171] "Starting Kubernetes Scheduler" version="v1.33.1"
I0615 20:01:22.006185       1 server.go:173] "Golang settings" GOGC="" GOMAXPROCS="" GOTRACEBACK=""
I0615 20:01:22.012976       1 configmap_cafile_content.go:205] "Starting controller" name="client-ca::kube-system::extension-apiserver-authentication::client-ca-file"
I0615 20:01:22.013095       1 shared_informer.go:350] "Waiting for caches to sync" controller="client-ca::kube-system::extension-apiserver-authentication::client-ca-file"
I0615 20:01:22.015094       1 secure_serving.go:211] Serving securely on 127.0.0.1:10259
E0615 20:01:22.015145       1 reflector.go:200] "Failed to watch" err="failed to list *v1.ConfigMap: Get \"https://192.168.1.161:6443/api/v1/namespaces/kube-system/configmaps?fieldSelector=metadata.name%3Dextension-apiserver-authentication&limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="runtime/asm_amd64.s:1700" type="*v1.ConfigMap"
I0615 20:01:22.015495       1 tlsconfig.go:243] "Starting DynamicServingCertificateController"
E0615 20:01:22.023996       1 reflector.go:200] "Failed to watch" err="failed to list *v1.ReplicaSet: Get \"https://192.168.1.161:6443/apis/apps/v1/replicasets?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.ReplicaSet"
E0615 20:01:22.024579       1 reflector.go:200] "Failed to watch" err="failed to list *v1.Service: Get \"https://192.168.1.161:6443/api/v1/services?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.Service"
E0615 20:01:22.025091       1 reflector.go:200] "Failed to watch" err="failed to list *v1.StatefulSet: Get \"https://192.168.1.161:6443/apis/apps/v1/statefulsets?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.StatefulSet"
E0615 20:01:22.026061       1 reflector.go:200] "Failed to watch" err="failed to list *v1.VolumeAttachment: Get \"https://192.168.1.161:6443/apis/storage.k8s.io/v1/volumeattachments?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.VolumeAttachment"
E0615 20:01:22.026648       1 reflector.go:200] "Failed to watch" err="failed to list *v1.CSIDriver: Get \"https://192.168.1.161:6443/apis/storage.k8s.io/v1/csidrivers?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.CSIDriver"
E0615 20:01:22.026998       1 reflector.go:200] "Failed to watch" err="failed to list *v1.PersistentVolumeClaim: Get \"https://192.168.1.161:6443/api/v1/persistentvolumeclaims?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.PersistentVolumeClaim"
E0615 20:01:22.027606       1 reflector.go:200] "Failed to watch" err="failed to list *v1.ReplicationController: Get \"https://192.168.1.161:6443/api/v1/replicationcontrollers?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.ReplicationController"
E0615 20:01:22.028099       1 reflector.go:200] "Failed to watch" err="failed to list *v1.Node: Get \"https://192.168.1.161:6443/api/v1/nodes?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.Node"
E0615 20:01:22.028552       1 reflector.go:200] "Failed to watch" err="failed to list *v1.PodDisruptionBudget: Get \"https://192.168.1.161:6443/apis/policy/v1/poddisruptionbudgets?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.PodDisruptionBudget"
E0615 20:01:22.029092       1 reflector.go:200] "Failed to watch" err="failed to list *v1.StorageClass: Get \"https://192.168.1.161:6443/apis/storage.k8s.io/v1/storageclasses?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.StorageClass"
E0615 20:01:22.029241       1 reflector.go:200] "Failed to watch" err="failed to list *v1.CSIStorageCapacity: Get \"https://192.168.1.161:6443/apis/storage.k8s.io/v1/csistoragecapacities?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.CSIStorageCapacity"
E0615 20:01:22.029831       1 reflector.go:200] "Failed to watch" err="failed to list *v1.Namespace: Get \"https://192.168.1.161:6443/api/v1/namespaces?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.Namespace"
E0615 20:01:22.030180       1 reflector.go:200] "Failed to watch" err="failed to list *v1.Pod: Get \"https://192.168.1.161:6443/api/v1/pods?fieldSelector=status.phase%21%3DSucceeded%2Cstatus.phase%21%3DFailed&limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.Pod"
E0615 20:01:22.030491       1 reflector.go:200] "Failed to watch" err="failed to list *v1.CSINode: Get \"https://192.168.1.161:6443/apis/storage.k8s.io/v1/csinodes?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.CSINode"
E0615 20:01:22.032279       1 reflector.go:200] "Failed to watch" err="failed to list *v1.PersistentVolume: Get \"https://192.168.1.161:6443/api/v1/persistentvolumes?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.PersistentVolume"
E0615 20:01:22.864041       1 reflector.go:200] "Failed to watch" err="failed to list *v1.Node: Get \"https://192.168.1.161:6443/api/v1/nodes?limit=500&resourceVersion=0\": dial tcp 192.168.1.161:6443: connect: connection refused" logger="UnhandledError" reflector="k8s.io/client-go/informers/factory.go:160" type="*v1.Node"
```


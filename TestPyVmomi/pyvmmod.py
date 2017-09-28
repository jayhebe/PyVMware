from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

import ssl

def connect_viserver(hostname, username, password):
    try:
        si = SmartConnect(host = hostname, user = username, pwd = password)
    except:
        context = None
        
        if hasattr(ssl, "_create_unverified_context"):
            context = ssl._create_unverified_context()
            
        si = SmartConnect(host = hostname, user = username, pwd = password, sslContext = context)
        
    return si

def disconnect_viserver(si):
    Disconnect(si)

# def get_datacenter(si):
#     dcs = []
#      
#     if isinstance(si, vim.ServiceInstance):
#         content = si.RetrieveContent()
#          
#         if hasattr(content, "rootFolder"):
#             for dc in content.rootFolder.childEntity:
#                 if isinstance(dc, vim.Datacenter):
#                     dcs.append(dc)
#             return dcs
#         else:
#             return None
#     else:
#         return None
#  
# def get_cluster(si):
#     clusters = []
#     dcs = get_datacenter(si)
#      
#     if dcs is not None:
#         for dc in dcs:
#             if hasattr(dc, "hostFolder"):
#                 for cluster in dc.hostFolder.childEntity:
#                     #if isinstance(cluster, vim.ComputeResource):
#                     clusters.append(cluster)
#                      
#         return clusters
#     else:
#         return None
#          
# def get_host(si):
#     hosts = []
#     clusters = get_cluster(si)
#      
#     if clusters is not None:
#         for cluster in clusters:
#             for host in cluster.host:
#                 hosts.append(host)
#         return hosts
#     else:
#         return None
#      
# def get_vm(si):
#     vms = []
#     hosts = get_host(si)
#      
#     if hosts is not None:
#         for host in hosts:
#             for vm in host.vm:
#                 vms.append(vm)
#         return vms
#     else:
#         return None

def get_objview(si, obj_type):
    if si is not None:
        content = si.RetrieveContent()
         
        if hasattr(content, "rootFolder"):
            return content.viewManager.CreateContainerView(content.rootFolder, obj_type, True).view
        else:
            return None
    else:
        return None
     
def get_datacenter(si):
    obj_dcs = []
     
    for obj_dc in get_objview(si, [vim.Datacenter]):
        obj_dcs.append(obj_dc)
         
    return obj_dcs
 
def get_cluster(si):
    obj_clusters = []
     
    for obj_cluster in get_objview(si, [vim.ComputeResource]):
        obj_clusters.append(obj_cluster)
         
    return obj_clusters
 
def get_host(si):
    obj_hosts = []
     
    for obj_host in get_objview(si, [vim.HostSystem]):
        obj_hosts.append(obj_host)
         
    return obj_hosts
     
def get_vm(si, vmname = None):
    if ( vmname is not None ) and ( vmname != "" ):
        for obj_vm in get_objview(si, [vim.VirtualMachine]):
            if obj_vm.name == vmname:
                return obj_vm
    else:
        obj_vms = []
        
        for obj_vm in get_objview(si, [vim.VirtualMachine]):
            obj_vms.append(obj_vm)
            
        return obj_vms
    

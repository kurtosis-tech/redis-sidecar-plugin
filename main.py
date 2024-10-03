def create_flow(service_spec, pod_spec, flow_uuid):
    pod_spec['containers'][0]["image"] = "kurtosistech/redis-proxy-overlay:latest"
    return {
        "pod_spec": pod_spec,
        "config_map": {}
    }

def delete_flow(config_map, flow_uuid):
    pass

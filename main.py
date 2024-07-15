def create_flow(service_spec, deployment_spec, flow_uuid):
    deployment_spec['template']['spec']['containers'][0]["image"] = "kurtosistech/redis-proxy-overlay:latest"
    return {
        "deployment_spec": deployment_spec,
        "config_map": {}
    }

def delete_flow(config_map, flow_uuid):
    pass

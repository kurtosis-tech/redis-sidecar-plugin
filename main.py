import copy


def create_flow(service_specs: list, pod_specs: list, flow_uuid):
    modified_pod_specs = []

    for pod_spec in pod_specs:
        modified_pod_spec = copy.deepcopy(pod_spec)
        modified_pod_spec['containers'][0]["image"] = "kurtosistech/redis-proxy-overlay:latest"

        modified_pod_specs.append(modified_pod_spec)

    return {
        "pod_specs": modified_pod_specs,
        "config_map": {}
    }


def delete_flow(config_map, flow_uuid):
    pass

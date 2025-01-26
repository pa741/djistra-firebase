<script>
    // @ts-ignore
    import { latLng } from "leaflet";
    import { Polyline } from "sveaflet";

    let { calle } = $props();
    let coords = JSON.parse(calle.geo);
    let isWarehouse = calle.warehouse;
    let isClient = calle.client;
    let c = [];
    for (let i = 0; i < coords.length; i++) {
        c.push(latLng(coords[i][1], coords[i][0]));
    }
    let color = isWarehouse ? "red" : isClient ? "green" : "#3388ff";

    console.log(c);
</script>

<Polyline latLngs={c} options={{ color: color }} />

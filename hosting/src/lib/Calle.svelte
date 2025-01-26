<script>
    // @ts-ignore
    import { latLng } from "leaflet";
    import { Polyline } from "sveaflet";

    let { calle } = $props();
    let coords = JSON.parse(calle.geo);
    let id = calle.id;
    let isWarehouse = calle.warehouse;
    let isClient = calle.client;
    let c = [];
    for (let i = 0; i < coords.length; i++) {
        c.push(latLng(coords[i][1], coords[i][0]));
    }
    let color = isWarehouse ? "red" : isClient ? "green" : "#3388ff";

    function handleClick() {
        console.log("Clicked, id: ", id);
    }
    
</script>

<Polyline onclick={handleClick}  latLngs={c} options={{ color: color }} />

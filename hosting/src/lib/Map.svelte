<script lang="ts">
    import { onMount, onDestroy } from "svelte";
    import { Map, TileLayer, Marker, Popup, Circle, CircleMarker, Polyline } from 'sveaflet';
    import { Collection } from "sveltefire";
    import Calle from "./Calle.svelte";



    const apiKey = "9AzDlyCvfhMjvdcFnJNT";

    onMount(() => {
        const initialState = {
            lng: -2.5630900924838076,
            lat: 42.46680422098594,
            zoom: 15,
        };



       
    });

    onDestroy(() => {
        console.log("destroying map");
    });
</script>

<div class="map-wrap">
    <Map
    options={{
      center: [42.46680422098594, -2.5630900924838076],
      zoom: 17
    }}
  >
    <TileLayer
        url={`https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=${apiKey}`}
        id="mapbox/streets-v11"
    />
<!---->
    <Collection ref={"Nodo"} let:data>
        {#each data as nodo}
            <CircleMarker
            latLng={[nodo.y, nodo.x]}
            >
            </CircleMarker>
        {/each}
    
        
    </Collection> 
<!---->
    <Collection ref={"Calle"} let:data>
        {#each data as calle}
        <Calle calle={calle} />
        {/each}
    
        
    </Collection>
  </Map>
</div>

<style>
    .map-wrap {
        position: relative;
        width: 100%;
        height: calc(
            100vh - 77px
        ); /* calculate height of the screen minus the heading */
    }

</style>

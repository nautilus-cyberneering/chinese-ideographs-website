<script>
	export let image_files = []
	console.log(image_files)
</script>

<main>
	<h1>Chinese Ideographs</h1>

	<h2>Base Drawings</h2>
	
	<ul>
		{#each image_files as { id, filename }, i}
		<li><a terget="_blank" href="./images/{filename}">{filename}</a></li>
		{/each}
	</ul>

</main>

<style>
	main {
		text-align: left;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}	
</style>
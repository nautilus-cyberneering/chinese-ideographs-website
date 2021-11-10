<script>
	export let image_files = []
	console.log(image_files)
</script>

<main>
	<h1>Chinese Ideographs</h1>

	<h2>Base Drawings</h2>
	
	<div class="gallery">

		{#each image_files as { id, filename }, i}
			{#if filename.endsWith(".jpg") }
			<div class="item">
				<a target="_blank" href="./images/{filename}">
					<img src="./images/{filename}" alt="{filename}" />
					<span>{filename}</span>
				</a>
			</div>
			{/if}
		{/each}

	</div>

</main>

<style>
	main {
		text-align: left;
		padding: 1em;
		margin: 0 auto;
	}

	.gallery {
		display: flex;
		flex-wrap: wrap;
	}

	.item {
		margin: 15px;
	}

	.item a {
		display: flex;	
		flex-direction: column;
		align-items: center;
	}

	.item a img {
		height: 180px;
	}

	.item a span {
		color: black;
		margin-top: 10px;
		font-size: 0.9em;
	}

	h1 {
		color: #909090;
		font-size: 4em;
		font-weight: 100;
		margin-top: 0;
		padding-top: 0;
		padding-bottom: 8px;
		margin-bottom: 8px;
	}

	h2 {
		padding-top: 0;
		margin-top: 0;
	} 

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}	
</style>
import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		image_files: JSON.parse(IMAGE_FILE_LIST_IN_JSON)
	}
});

export default app;
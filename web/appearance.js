import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "Bori-KontextPresets.appearance", // Extension name
    async nodeCreated(node) {
		console.log("Checking node:", node.comfyClass);
        // Check if the node's comfyClass starts with "Bori Kontext Presets"
        if (node.comfyClass.startsWith("Bori Kontext Presets")) {
            // Apply styling
            node.color = "#EEE8AA";
            node.bgcolor = "#FFDAB9";
			console.log("Colorized:", node.comfyClass);
        }
    }
});
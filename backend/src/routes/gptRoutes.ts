import express, { Request, Response } from "express";
import OpenAI from "openai";
import dotenv from "dotenv";

// dotenv.config({ path: "../.env" });

const gptRouter = express.Router();

// Initialize OpenAI client
const openai = new OpenAI({
  apiKey:
    "Your key here.",
});

interface GenerateRequest {
  layout: string;
  color_theme: string;
  pages: string[];
  items: string[];
  interactivity?: string[];
}

gptRouter.post(
  "/",
  async (
    req: Request<{}, {}, GenerateRequest>,
    res: Response
  ): Promise<any> => {
    const { layout, color_theme, pages, items, interactivity } = req.body;
    const prompt = `
Generate a complete, responsive ecommerce website using HTML, CSS, and JavaScript only.
- Layout: ${layout}
- Color theme: ${color_theme}
- Pages: ${pages.join(", ")}
- Products/items: ${items.join(", ")}
${interactivity ? `- Interactivity features: ${interactivity.join(", ")}` : ""}
Output the entire code (one HTML file with embedded <style> and <script>), without any explanation.
`;

    try {
      const completion = await openai.chat.completions.create({
        model: "gpt-3.5-turbo", // or "gpt-3.5-turbo"
        messages: [{ role: "user", content: prompt }],
        temperature: 0.7,
        max_tokens: 2000,
      });
      const html = completion.choices[0].message.content;

      if (!html) {
        return res.status(500).json({ error: "Empty response from GPT" });
      }

      res.json({ html });
    } catch (err: any) {
      console.error("OpenAI Error:", err);
      res.status(500).json({ error: err.message || "Generation failed" });
    }
  }
);

export default gptRouter;

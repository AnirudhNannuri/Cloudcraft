import mongoose, { Document, Schema, Types } from "mongoose";

export interface IProject extends Document {
  userId: Types.ObjectId;
  name: string;
  prompt: {
    layout: string;
    color_theme: string;
    pages: string[];
    items: string[];
    interactivity?: string[];
  };
  html: string;
  createdAt: Date;
}

const ProjectSchema = new Schema<IProject>({
  userId:   { type: Schema.Types.ObjectId, ref: "User", required: true },
  name:     { type: String, required: true },
  prompt: {
    layout:      { type: String, required: true },
    color_theme: { type: String, required: true },
    pages:       [String],
    items:       [String],
    interactivity: [String],
  },
  html:      { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
}, {
    collection: "generated-websites"
});

export default mongoose.model<IProject>("Project", ProjectSchema);

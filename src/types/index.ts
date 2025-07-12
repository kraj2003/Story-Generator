export interface StoryParams {
  prompt: string;
  genre: 'Fantasy' | 'Science Fiction' | 'Mystery/Thriller' | 'Romance' | 'Horror' | 'Adventure' | 'Comedy' | 'Drama';
  length: 'Short' | 'Medium' | 'Long';
  tone: string;
  pov: 'First Person' | 'Third Person';
  creativityLevel: number;
  complexity: string;
  timePeriod?: string;
  emotionalCore?: string;
  narrativeStructure?: string;
  includeTwist?: boolean;
}

export interface GeneratedStory extends StoryParams {
  id: string;
  content: string;
  wordCount: number;
  createdAt: string;
}

export interface StoryAnalytics {
  wordCount: number;
  sentenceCount: number;
  paragraphCount: number;
  avgSentenceLength: number;
  dialogueCount: number;
  readTime: number;
}
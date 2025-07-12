import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Wand2, Settings, ChevronDown, Lightbulb } from 'lucide-react';
import { StoryParams } from '../types';
import LoadingSpinner from './LoadingSpinner';

interface StoryFormProps {
  onGenerate: (params: StoryParams) => void;
  isGenerating: boolean;
}

const StoryForm: React.FC<StoryFormProps> = ({ onGenerate, isGenerating }) => {
  const [params, setParams] = useState<StoryParams>({
    prompt: '',
    genre: 'Fantasy',
    length: 'Medium',
    tone: 'Neutral',
    pov: 'Third Person',
    creativityLevel: 0.7,
    complexity: 'Layered',
    timePeriod: 'Contemporary',
    emotionalCore: 'Discovery',
    narrativeStructure: 'Linear',
    includeTwist: true,
  });

  const [showAdvanced, setShowAdvanced] = useState(false);

  const genres = [
    'Fantasy', 'Science Fiction', 'Mystery/Thriller', 'Romance',
    'Horror', 'Adventure', 'Comedy', 'Drama'
  ];

  const tones = ['Neutral', 'Dark', 'Light-hearted', 'Dramatic', 'Humorous'];
  const complexities = ['Straightforward', 'Layered', 'Complex'];
  const timePeriods = ['Contemporary', 'Historical', 'Future', 'Timeless'];
  const emotionalCores = ['Love', 'Loss', 'Discovery', 'Redemption', 'Survival', 'Growth', 'Justice', 'Freedom'];
  const narrativeStructures = ['Linear', 'Flashbacks', 'Multiple Timeline', 'Circular'];

  const examplePrompts = {
    Fantasy: "A librarian discovers that every book they touch reveals the true fate of its previous readers",
    'Science Fiction': "Memory merchants sell experiences to the highest bidder, but one memory refuses to be sold",
    'Mystery/Thriller': "A forensic accountant finds their own signature on documents from before they were born",
    Romance: "Two people keep meeting in dreams before they meet in real life",
    Horror: "A child's imaginary friend starts leaving physical evidence of their existence",
    Adventure: "A cartographer discovers their maps are changing to show places that don't exist yet",
    Comedy: "A professional mourner accidentally attends the wrong funeral and can't escape",
    Drama: "A parent finds their estranged child's diary and realizes they never knew them at all"
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (params.prompt.trim()) {
      onGenerate(params);
    }
  };

  const handleUseExample = () => {
    setParams(prev => ({
      ...prev,
      prompt: examplePrompts[prev.genre as keyof typeof examplePrompts] || ''
    } as StoryParams));
  };

  return (
    <motion.div
      initial={{ opacity: 0, x: -20 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.6 }}
      className="glass-card rounded-2xl p-8"
    >
      <div className="flex items-center gap-3 mb-6">
        <Wand2 className="text-primary-600" size={28} />
        <h2 className="text-2xl font-bold text-gray-800">Story Vision</h2>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Story Prompt */}
        <div>
          <label className="block text-sm font-semibold text-gray-700 mb-2">
            Your Story Concept
          </label>
          <div className="relative">
            <textarea
              value={params.prompt}
              onChange={(e) => setParams(prev => ({ ...prev, prompt: e.target.value }))}
              placeholder={`Inspiration: ${examplePrompts[params.genre as keyof typeof examplePrompts]}`}
              className="input-field h-32 resize-none"
              required
            />
            <button
              type="button"
              onClick={handleUseExample}
              className="absolute top-2 right-2 text-xs bg-primary-100 text-primary-700 px-2 py-1 rounded-md hover:bg-primary-200 transition-colors flex items-center gap-1"
            >
              <Lightbulb size={12} />
              Use Example
            </button>
          </div>
        </div>

        {/* Basic Settings */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              Genre Expertise
            </label>
            <select
              value={params.genre}
              onChange={(e) => setParams(prev => ({ ...prev, genre: e.target.value }))}
              className="select-field"
            >
              {genres.map(genre => (
                <option key={genre} value={genre}>{genre}</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              Story Depth
            </label>
            <select
              value={params.length}
              onChange={(e) => setParams(prev => ({ ...prev, length: e.target.value as 'Short' | 'Medium' | 'Long' }))}
              className="select-field"
            >
              <option value="Short">Short (600-800 words)</option>
              <option value="Medium">Medium (1200-1500 words)</option>
              <option value="Long">Long (2000-2500 words)</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              Emotional Tone
            </label>
            <select
              value={params.tone}
              onChange={(e) => setParams(prev => ({ ...prev, tone: e.target.value }))}
              className="select-field"
            >
              {tones.map(tone => (
                <option key={tone} value={tone}>{tone}</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              Narrative Perspective
            </label>
            <select
              value={params.pov}
              onChange={(e) => setParams(prev => ({ ...prev, pov: e.target.value as 'First Person' | 'Third Person' }))}
              className="select-field"
            >
              <option value="First Person">First Person</option>
              <option value="Third Person">Third Person</option>
            </select>
          </div>
        </div>

        {/* Creativity Level */}
        <div>
          <label className="block text-sm font-semibold text-gray-700 mb-2">
            Creative Risk Level: {Math.round(params.creativityLevel * 100)}%
          </label>
          <input
            type="range"
            min="0.1"
            max="1.0"
            step="0.1"
            value={params.creativityLevel}
            onChange={(e) => setParams(prev => ({ ...prev, creativityLevel: parseFloat(e.target.value) }))}
            className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
          />
          <div className="flex justify-between text-xs text-gray-500 mt-1">
            <span>Safe & Coherent</span>
            <span>Balanced</span>
            <span>Bold & Experimental</span>
          </div>
        </div>

        {/* Advanced Options */}
        <div>
          <button
            type="button"
            onClick={() => setShowAdvanced(!showAdvanced)}
            className="flex items-center gap-2 text-primary-600 hover:text-primary-700 font-medium transition-colors"
          >
            <Settings size={16} />
            Advanced Story Elements
            <ChevronDown 
              size={16} 
              className={`transform transition-transform ${showAdvanced ? 'rotate-180' : ''}`}
            />
          </button>

          {showAdvanced && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4"
            >
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Time Period
                </label>
                <select
                  value={params.timePeriod}
                  onChange={(e) => setParams(prev => ({ ...prev, timePeriod: e.target.value }))}
                  className="select-field"
                >
                  {timePeriods.map(period => (
                    <option key={period} value={period}>{period}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Emotional Core
                </label>
                <select
                  value={params.emotionalCore}
                  onChange={(e) => setParams(prev => ({ ...prev, emotionalCore: e.target.value }))}
                  className="select-field"
                >
                  {emotionalCores.map(core => (
                    <option key={core} value={core}>{core}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Narrative Structure
                </label>
                <select
                  value={params.narrativeStructure}
                  onChange={(e) => setParams(prev => ({ ...prev, narrativeStructure: e.target.value }))}
                  className="select-field"
                >
                  {narrativeStructures.map(structure => (
                    <option key={structure} value={structure}>{structure}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Narrative Complexity
                </label>
                <select
                  value={params.complexity}
                  onChange={(e) => setParams(prev => ({ ...prev, complexity: e.target.value }))}
                  className="select-field"
                >
                  {complexities.map(complexity => (
                    <option key={complexity} value={complexity}>{complexity}</option>
                  ))}
                </select>
              </div>

              <div className="md:col-span-2">
                <label className="flex items-center gap-2 text-sm font-semibold text-gray-700">
                  <input
                    type="checkbox"
                    checked={params.includeTwist}
                    onChange={(e) => setParams(prev => ({ ...prev, includeTwist: e.target.checked }))}
                    className="rounded border-gray-300 text-primary-600 focus:ring-primary-500"
                  />
                  Include Plot Twist
                </label>
              </div>
            </motion.div>
          )}
        </div>

        {/* Generate Button */}
        <button
          type="submit"
          disabled={isGenerating || !params.prompt.trim()}
          className="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
        >
          {isGenerating ? (
            <div className="flex items-center justify-center gap-3">
              <LoadingSpinner />
              Creating Masterpiece...
            </div>
          ) : (
            <div className="flex items-center justify-center gap-2">
              <Wand2 size={20} />
              Create Masterpiece
            </div>
          )}
        </button>
      </form>
    </motion.div>
  );
};

export default StoryForm;
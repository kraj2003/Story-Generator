import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { BookOpen, Copy, Download, Heart, BarChart3, Clock, FileText } from 'lucide-react';
import { GeneratedStory } from '../types';

interface StoryDisplayProps {
  story: GeneratedStory;
  onSave: (story: GeneratedStory) => void;
}

const StoryDisplay: React.FC<StoryDisplayProps> = ({ story, onSave }) => {
  const [showAnalytics, setShowAnalytics] = useState(false);
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(story.content);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
    }
  };

  const handleDownload = () => {
    const element = document.createElement('a');
    const file = new Blob([story.content], { type: 'text/plain' });
    element.href = URL.createObjectURL(file);
    element.download = `story-${story.genre.toLowerCase()}-${Date.now()}.txt`;
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  };

  const analytics = {
    sentenceCount: story.content.split(/[.!?]+/).filter(s => s.trim().length > 0).length,
    paragraphCount: story.content.split('\n\n').filter(p => p.trim().length > 0).length,
    avgSentenceLength: Math.round(story.wordCount / (story.content.split(/[.!?]+/).filter(s => s.trim().length > 0).length || 1)),
    readTime: Math.max(1, Math.round(story.wordCount / 200)),
    dialogueCount: (story.content.match(/"/g) || []).length / 2,
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="glass-card rounded-2xl p-6"
    >
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <BookOpen className="text-primary-600" size={24} />
          <h3 className="text-xl font-bold text-gray-800">Your Masterpiece</h3>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-sm bg-primary-100 text-primary-700 px-2 py-1 rounded-full">
            {story.genre}
          </span>
        </div>
      </div>

      {/* Story Content */}
      <div className="bg-gradient-to-br from-gray-50 to-blue-50 rounded-xl p-6 mb-6 border border-gray-100">
        <div className="story-text whitespace-pre-line">
          {story.content}
        </div>
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-2 gap-4 mb-6">
        <div className="bg-white/60 rounded-lg p-3 text-center">
          <div className="text-2xl font-bold text-primary-600">{story.wordCount}</div>
          <div className="text-sm text-gray-600">Words</div>
        </div>
        <div className="bg-white/60 rounded-lg p-3 text-center">
          <div className="text-2xl font-bold text-accent-600">{analytics.readTime}</div>
          <div className="text-sm text-gray-600">Min Read</div>
        </div>
      </div>

      {/* Analytics Toggle */}
      <button
        onClick={() => setShowAnalytics(!showAnalytics)}
        className="w-full mb-4 flex items-center justify-center gap-2 text-primary-600 hover:text-primary-700 font-medium transition-colors"
      >
        <BarChart3 size={16} />
        {showAnalytics ? 'Hide' : 'Show'} Analytics
      </button>

      {/* Detailed Analytics */}
      {showAnalytics && (
        <motion.div
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: 'auto' }}
          exit={{ opacity: 0, height: 0 }}
          className="grid grid-cols-2 gap-3 mb-6 text-sm"
        >
          <div className="bg-white/60 rounded-lg p-3">
            <div className="font-semibold text-gray-700">Sentences</div>
            <div className="text-lg font-bold text-primary-600">{analytics.sentenceCount}</div>
          </div>
          <div className="bg-white/60 rounded-lg p-3">
            <div className="font-semibold text-gray-700">Paragraphs</div>
            <div className="text-lg font-bold text-primary-600">{analytics.paragraphCount}</div>
          </div>
          <div className="bg-white/60 rounded-lg p-3">
            <div className="font-semibold text-gray-700">Avg Sentence</div>
            <div className="text-lg font-bold text-primary-600">{analytics.avgSentenceLength}</div>
          </div>
          <div className="bg-white/60 rounded-lg p-3">
            <div className="font-semibold text-gray-700">Dialogue</div>
            <div className="text-lg font-bold text-primary-600">{Math.round(analytics.dialogueCount)}</div>
          </div>
        </motion.div>
      )}

      {/* Action Buttons */}
      <div className="grid grid-cols-2 gap-3">
        <button
          onClick={handleCopy}
          className="btn-secondary flex items-center justify-center gap-2"
        >
          <Copy size={16} />
          {copied ? 'Copied!' : 'Copy'}
        </button>
        <button
          onClick={handleDownload}
          className="btn-secondary flex items-center justify-center gap-2"
        >
          <Download size={16} />
          Download
        </button>
        <button
          onClick={() => onSave(story)}
          className="btn-primary col-span-2 flex items-center justify-center gap-2"
        >
          <Heart size={16} />
          Save Masterpiece
        </button>
      </div>
    </motion.div>
  );
};

export default StoryDisplay;
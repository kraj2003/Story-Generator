import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Library, Trash2, Eye, Filter, Calendar, BookOpen } from 'lucide-react';
import { GeneratedStory } from '../types';

interface SavedStoriesProps {
  stories: GeneratedStory[];
  onDelete: (id: string) => void;
}

const SavedStories: React.FC<SavedStoriesProps> = ({ stories, onDelete }) => {
  const [selectedStory, setSelectedStory] = useState<GeneratedStory | null>(null);
  const [filterGenre, setFilterGenre] = useState<string>('All');
  const [sortBy, setSortBy] = useState<'recent' | 'wordCount' | 'genre'>('recent');

  const genres = ['All', ...Array.from(new Set(stories.map(story => story.genre)))];

  const filteredStories = stories
    .filter(story => filterGenre === 'All' || story.genre === filterGenre)
    .sort((a, b) => {
      switch (sortBy) {
        case 'recent':
          return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
        case 'wordCount':
          return b.wordCount - a.wordCount;
        case 'genre':
          return a.genre.localeCompare(b.genre);
        default:
          return 0;
      }
    });

  if (stories.length === 0) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="glass-card rounded-2xl p-6 text-center"
      >
        <Library className="mx-auto text-gray-400 mb-4" size={48} />
        <h3 className="text-lg font-semibold text-gray-600 mb-2">No Saved Stories</h3>
        <p className="text-gray-500">Create your first masterpiece to get started!</p>
      </motion.div>
    );
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="glass-card rounded-2xl p-6"
    >
      <div className="flex items-center gap-2 mb-6">
        <Library className="text-primary-600" size={24} />
        <h3 className="text-xl font-bold text-gray-800">
          Your Library ({stories.length})
        </h3>
      </div>

      {/* Filters */}
      <div className="flex flex-col sm:flex-row gap-3 mb-6">
        <select
          value={filterGenre}
          onChange={(e) => setFilterGenre(e.target.value)}
          className="select-field text-sm"
        >
          {genres.map(genre => (
            <option key={genre} value={genre}>{genre}</option>
          ))}
        </select>
        <select
          value={sortBy}
          onChange={(e) => setSortBy(e.target.value as 'recent' | 'wordCount' | 'genre')}
          className="select-field text-sm"
        >
          <option value="recent">Recent</option>
          <option value="wordCount">Word Count</option>
          <option value="genre">Genre</option>
        </select>
      </div>

      {/* Stories List */}
      <div className="space-y-3 max-h-96 overflow-y-auto">
        <AnimatePresence>
          {filteredStories.map((story, index) => (
            <motion.div
              key={story.id}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: 20 }}
              transition={{ duration: 0.3, delay: index * 0.1 }}
              className="bg-white/60 rounded-lg p-4 border border-gray-100 hover:shadow-md transition-shadow"
            >
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-xs bg-primary-100 text-primary-700 px-2 py-1 rounded-full">
                      {story.genre}
                    </span>
                    <span className="text-xs text-gray-500">
                      {new Date(story.createdAt).toLocaleDateString()}
                    </span>
                  </div>
                  <p className="text-sm text-gray-700 mb-2 line-clamp-2">
                    {story.prompt.substring(0, 100)}...
                  </p>
                  <div className="flex items-center gap-4 text-xs text-gray-500">
                    <span className="flex items-center gap-1">
                      <BookOpen size={12} />
                      {story.wordCount} words
                    </span>
                    <span>{story.length}</span>
                    <span>{story.tone}</span>
                  </div>
                </div>
                <div className="flex gap-2 ml-4">
                  <button
                    onClick={() => setSelectedStory(story)}
                    className="p-2 text-primary-600 hover:bg-primary-50 rounded-lg transition-colors"
                    title="View Story"
                  >
                    <Eye size={16} />
                  </button>
                  <button
                    onClick={() => onDelete(story.id)}
                    className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                    title="Delete Story"
                  >
                    <Trash2 size={16} />
                  </button>
                </div>
              </div>
            </motion.div>
          ))}
        </AnimatePresence>
      </div>

      {/* Story Modal */}
      <AnimatePresence>
        {selectedStory && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50"
            onClick={() => setSelectedStory(null)}
          >
            <motion.div
              initial={{ scale: 0.9, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.9, opacity: 0 }}
              className="bg-white rounded-2xl p-6 max-w-4xl max-h-[80vh] overflow-y-auto"
              onClick={(e) => e.stopPropagation()}
            >
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h3 className="text-xl font-bold text-gray-800">{selectedStory.genre} Story</h3>
                  <p className="text-sm text-gray-600">
                    Created {new Date(selectedStory.createdAt).toLocaleDateString()}
                  </p>
                </div>
                <button
                  onClick={() => setSelectedStory(null)}
                  className="text-gray-500 hover:text-gray-700"
                >
                  ✕
                </button>
              </div>
              
              <div className="mb-4 p-3 bg-gray-50 rounded-lg">
                <p className="text-sm text-gray-700">
                  <strong>Prompt:</strong> {selectedStory.prompt}
                </p>
              </div>
              
              <div className="story-text whitespace-pre-line bg-gradient-to-br from-gray-50 to-blue-50 rounded-xl p-6 border border-gray-100">
                {selectedStory.content}
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
};

export default SavedStories;
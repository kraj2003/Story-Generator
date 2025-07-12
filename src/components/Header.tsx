import React from 'react';
import { motion } from 'framer-motion';
import { BookOpen, Sparkles, Wand2 } from 'lucide-react';

const Header: React.FC = () => {
  return (
    <header className="bg-gradient-to-r from-primary-600 via-primary-700 to-accent-600 text-white">
      <div className="container mx-auto px-4 py-8">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-center"
        >
          <div className="flex items-center justify-center gap-3 mb-4">
            <motion.div
              animate={{ rotate: 360 }}
              transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
            >
              <BookOpen size={48} className="text-white" />
            </motion.div>
            <h1 className="text-4xl md:text-6xl font-bold">
              AI Story Generator Pro
            </h1>
            <motion.div
              animate={{ scale: [1, 1.2, 1] }}
              transition={{ duration: 2, repeat: Infinity }}
            >
              <Sparkles size={32} className="text-accent-200" />
            </motion.div>
          </div>
          
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.3, duration: 0.6 }}
            className="text-xl md:text-2xl text-primary-100 mb-6 max-w-3xl mx-auto"
          >
            Create exceptional stories with advanced AI prompting techniques
          </motion.p>
          
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.6, duration: 0.6 }}
            className="flex items-center justify-center gap-6 text-primary-200"
          >
            <div className="flex items-center gap-2">
              <Wand2 size={20} />
              <span>8 Genre Specializations</span>
            </div>
            <div className="hidden md:block w-px h-6 bg-primary-300"></div>
            <div className="flex items-center gap-2">
              <Sparkles size={20} />
              <span>Advanced AI Prompting</span>
            </div>
            <div className="hidden md:block w-px h-6 bg-primary-300"></div>
            <div className="flex items-center gap-2">
              <BookOpen size={20} />
              <span>Professional Quality</span>
            </div>
          </motion.div>
        </motion.div>
      </div>
    </header>
  );
};

export default Header;
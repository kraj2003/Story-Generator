import React from 'react';
import { motion } from 'framer-motion';
import { Heart, Github, Twitter, Mail } from 'lucide-react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gradient-to-r from-gray-900 to-gray-800 text-white mt-16">
      <div className="container mx-auto px-4 py-12">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="grid grid-cols-1 md:grid-cols-4 gap-8"
        >
          {/* Brand */}
          <div className="md:col-span-2">
            <h3 className="text-2xl font-bold mb-4 gradient-text">
              AI Story Generator Pro
            </h3>
            <p className="text-gray-300 mb-4 max-w-md">
              Transform your ideas into masterpieces with advanced AI prompting techniques. 
              Create exceptional stories across 8 specialized genres with professional-grade quality.
            </p>
            <div className="flex items-center gap-4">
              <a href="#" className="text-gray-400 hover:text-white transition-colors">
                <Github size={20} />
              </a>
              <a href="#" className="text-gray-400 hover:text-white transition-colors">
                <Twitter size={20} />
              </a>
              <a href="#" className="text-gray-400 hover:text-white transition-colors">
                <Mail size={20} />
              </a>
            </div>
          </div>

          {/* Features */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Features</h4>
            <ul className="space-y-2 text-gray-300">
              <li>8 Genre Specializations</li>
              <li>Advanced AI Prompting</li>
              <li>Professional Quality</li>
              <li>Story Analytics</li>
              <li>Export & Save</li>
            </ul>
          </div>

          {/* Genres */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Genres</h4>
            <ul className="space-y-2 text-gray-300">
              <li>Fantasy</li>
              <li>Science Fiction</li>
              <li>Mystery/Thriller</li>
              <li>Romance</li>
              <li>Horror</li>
              <li>Adventure</li>
              <li>Comedy</li>
              <li>Drama</li>
            </ul>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3, duration: 0.6 }}
          className="border-t border-gray-700 mt-8 pt-8 text-center"
        >
          <p className="text-gray-400 flex items-center justify-center gap-2">
            Built with <Heart size={16} className="text-red-500" /> for storytellers and AI enthusiasts
          </p>
          <p className="text-gray-500 text-sm mt-2">
            © 2025 AI Story Generator Pro. Powered by advanced prompting techniques.
          </p>
        </motion.div>
      </div>
    </footer>
  );
};

export default Footer;
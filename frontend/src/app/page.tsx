"use client";
import React, { useState } from 'react';
import { ShieldAlert, ShieldCheck, ShieldOff, Loader2, AlertTriangle } from 'lucide-react';

export default function RiskDashboard() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  const checkRisk = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/v1/assets/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          asset_type: "image",
          content_source: url || "https://example.com/placeholder.png",
          prompt: "Marketing campaign asset"
        }),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("API Error:", error);
      alert("Make sure your FastAPI backend is running on port 8000!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 p-8 font-sans">
      <div className="max-w-4xl mx-auto">
        <header className="mb-10 text-center">
          <h1 className="text-4xl font-bold text-slate-900 mb-2">🛡️ Brand Sentinel</h1>
          <p className="text-slate-500 text-lg">AI Content Governance & Risk Assessment</p>
        </header>

        {/* Input Section */}
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 mb-8">
          <label className="block text-sm font-semibold text-slate-700 mb-2">Asset URL to Analyze</label>
          <div className="flex gap-4">
            <input
              type="text"
              placeholder="https://content.ai/generated-image-01.png"
              className="flex-1 p-3 rounded-xl border border-slate-200 focus:ring-2 focus:ring-blue-500 outline-none transition-all"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
            <button
              onClick={checkRisk}
              disabled={loading}
              className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-xl font-bold flex items-center gap-2 transition-all disabled:opacity-50"
            >
              {loading ? <Loader2 className="animate-spin" /> : "Analyze Asset"}
            </button>
          </div>
        </div>

        {/* Results Section */}
        {result && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 animate-in fade-in slide-in-from-bottom-4">
            {/* Risk Meter Card */}
            <div className="md:col-span-1 bg-white p-6 rounded-2xl shadow-sm border border-slate-200 flex flex-col items-center justify-center">
              <span className="text-sm font-bold uppercase tracking-wider text-slate-400 mb-4">Risk Score</span>
              <div className={`text-6xl font-black mb-2 ${result.verdict === 'PASS' ? 'text-green-500' :
                  result.verdict === 'FLAG' ? 'text-amber-500' : 'text-red-500'
                }`}>
                {Math.round(result.risk_score)}
              </div>
              <div className="flex items-center gap-2 font-bold px-4 py-1 rounded-full bg-slate-100 uppercase text-xs">
                {result.verdict === 'PASS' && <ShieldCheck className="w-4 h-4 text-green-500" />}
                {result.verdict === 'FLAG' && <AlertTriangle className="w-4 h-4 text-amber-500" />}
                {result.verdict === 'BLOCK' && <ShieldOff className="w-4 h-4 text-red-500" />}
                {result.verdict}
              </div>
            </div>

            {/* Analysis Breakdown */}
            <div className="md:col-span-2 bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
              <h3 className="font-bold text-slate-800 mb-4">Risk Breakdown</h3>
              <div className="space-y-4">
                {[
                  { label: "Visual Similarity", value: result.breakdown.visual_similarity },
                  { label: "Text Leakage", value: result.breakdown.text_leakage },
                  { label: "Provenance Integrity", value: result.breakdown.provenance_risk },
                ].map((item) => (
                  <div key={item.label}>
                    <div className="flex justify-between text-sm mb-1">
                      <span className="text-slate-600">{item.label}</span>
                      <span className="font-mono font-bold">{item.value}%</span>
                    </div>
                    <div className="w-full bg-slate-100 rounded-full h-2">
                      <div
                        className="bg-blue-500 h-2 rounded-full transition-all duration-1000"
                        style={{ width: `${item.value}%` }}
                      ></div>
                    </div>
                  </div>
                ))}
              </div>
              <div className="mt-6 p-4 bg-blue-50 border border-blue-100 rounded-xl">
                <p className="text-sm text-blue-800 flex gap-2">
                  <ShieldAlert className="w-5 h-5 flex-shrink-0" />
                  <strong>Recommendation:</strong> {result.recommendation}
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
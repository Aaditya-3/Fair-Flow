import React, { useState } from "react";
import { extractCandidateFromResume } from "../api/fairlensApi";

export default function SampleExtract() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    setError(null);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const data = await extractCandidateFromResume(formData);
      setResult(data);
    } catch (err) {
      setError(err?.response?.data?.detail?.message || err.message || "Extraction failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white p-8">
      <div className="max-w-2xl mx-auto space-y-6">
        <h1 className="text-3xl font-bold">Resume Extraction Demo</h1>
        <p className="text-slate-400">Upload a resume to test the Gemini 1.5 Flash extraction model.</p>
        
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
          <input
            type="file"
            accept="image/png, image/jpeg, application/pdf"
            onChange={(e) => setFile(e.target.files[0])}
            className="block w-full text-sm text-slate-400
              file:mr-4 file:py-2 file:px-4
              file:rounded-full file:border-0
              file:text-sm file:font-semibold
              file:bg-orange-500/10 file:text-orange-500
              hover:file:bg-orange-500/20"
          />
          <button
            onClick={handleUpload}
            disabled={!file || loading}
            className="mt-4 w-full bg-orange-500 hover:bg-orange-600 disabled:opacity-50 text-white font-medium py-2 rounded-lg transition-colors"
          >
            {loading ? "Extracting with Gemini..." : "Extract Data"}
          </button>
        </div>

        {error && (
          <div className="bg-red-500/10 border border-red-500/50 text-red-400 p-4 rounded-xl">
            {error}
          </div>
        )}

        {result && (
          <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-4">
            <h2 className="text-xl font-semibold">Extraction Result</h2>
            <pre className="bg-slate-950 p-4 rounded-lg overflow-x-auto text-sm text-green-400">
              {JSON.stringify(result, null, 2)}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}

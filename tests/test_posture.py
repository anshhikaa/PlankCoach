from src.analysis.posture import PostureAnalyzer
analyser = PostureAnalyzer()
print(analyser.analyze(180))
print(analyser.analyze(None))
print(analyser.analyze(170))
print(analyser.analyze(150))
print(analyser.analyze(170))
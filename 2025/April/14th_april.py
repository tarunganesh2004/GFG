# Alien Dictionary

words=["baa","abcd","abca","cab","cad"]

def alienOrder(words):
    adj = {c: set() for word in words for c in word}
    indegree = {c: 0 for word in words for c in word}
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_length = min(len(w1), len(w2))
        
        for j in range(min_length):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break
        else:
            if len(w1) > len(w2):
                return ""
    
    queue = [c for c in indegree if indegree[c] == 0]
    order = []
    
    while queue:
        c = queue.pop(0)
        order.append(c)
        for neighbor in adj[c]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return "".join(order) if len(order) == len(indegree) else ""

print(alienOrder(words))
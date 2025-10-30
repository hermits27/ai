class BayesClassifier:
    def __init__(self, hypotheses, priors):
        """
        Initialize with hypotheses and their prior probabilities.
        
        hypotheses: list of hypothesis names (e.g., ['H1', 'H2', 'H3'])
        priors: dict mapping hypothesis -> prior probability, e.g., {'H1':0.3, 'H2':0.4, 'H3':0.3}
        """
        self.hypotheses = hypotheses
        self.priors = priors  # P(H)
        self.posterior = priors.copy()

    def update(self, evidence_likelihood):
        """
        Update posterior given evidence likelihoods.
        
        evidence_likelihood: dict mapping hypothesis -> P(E | hypothesis)
        """
        # Calculate unnormalized posteriors P(H) * P(E|H)
        unnormalized = {}
        for h in self.hypotheses:
            unnormalized[h] = self.posterior[h] * evidence_likelihood[h]
        
        # Normalization constant P(E)
        total = sum(unnormalized.values())
        if total == 0:
            raise ValueError("Total probability is zero, check likelihoods.")
        
        # Normalize to get new posterior P(H|E)
        for h in self.hypotheses:
            self.posterior[h] = unnormalized[h] / total

    def get_posterior(self):
        """Return current posterior probabilities."""
        return self.posterior

# Example usage:
if __name__ == "__main__":
    # Hypotheses: Diseases A, B, and No disease
    hypotheses = ['Disease A', 'Disease B', 'No Disease']

    # Priors: Initial beliefs about hypotheses
    priors = {
        'Disease A': 0.01,
        'Disease B': 0.005,
        'No Disease': 0.985
    }

    classifier = BayesClassifier(hypotheses, priors)

    # First evidence: Positive test result 1
    evidence1_likelihood = {
        'Disease A': 0.9,    # P(Positive test 1 | Disease A)
        'Disease B': 0.7,    # P(Positive test 1 | Disease B)
        'No Disease': 0.1    # P(Positive test 1 | No Disease)
    }
    classifier.update(evidence1_likelihood)
    print("Posterior after test 1:", classifier.get_posterior())

    # Second evidence: Positive test result 2
    evidence2_likelihood = {
        'Disease A': 0.8,    # P(Positive test 2 | Disease A)
        'Disease B': 0.6,    # P(Positive test 2 | Disease B)
        'No Disease': 0.05   # P(Positive test 2 | No Disease)
    }
    classifier.update(evidence2_likelihood)
    print("Posterior after test 2:", classifier.get_posterior())

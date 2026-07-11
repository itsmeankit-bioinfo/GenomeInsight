"""
GenomeInsight Pipeline Runner
"""


class Pipeline:

    def __init__(self):

        self.steps = []

    def add(self, name, function):

        self.steps.append((name, function))

    def run(self):

        print("\nGenomeInsight Pipeline")
        print("=" * 40)

        for name, function in self.steps:

            print(f"\nRunning {name}...")

            function()

        print("\nPipeline completed successfully.")
class Job {
    private int jobID, deadline, profit;

    public Job(int jobID, int deadline, int profit) {
        this.jobID = jobID;
        this.deadline = deadline;
        this.profit = profit;
    }

    public int getDeadline() {
        return deadline;
    }
    public int getProfit() {
        return profit;
    }
    public int getJobID() {
        return jobID;
    }
};

class JobSequence {
    public static int jobSequence(List<Job> jobs, int T) {
        int maxProfit = 0;
        int[] slot = new int[T];
        Arrays.fill(slot, -1);
        for (Job job : jobs) {
            for (int slotIndex = job.getDeadline() - 1; slotIndex >= 0; slotIndex--) {
                if (slotIndex < T && slot[slotIndex] != -1) {
                    slot[slotIndex] = job.getJobID();
                    maxProfit += job.getProfit;
                    break;
                }
            }
        }
        System.out.println("The Sequenced Jobs are: ");
        Arrays.stream(slot).filter(val -> val != 1).forEach(System.out::println);
        return maxProfit;

    }
}